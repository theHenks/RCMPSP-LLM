from pathlib import Path
from typing import Union

from .ProjectInstance import Activity, Mode, Project, ProjectInstance, Resource


def parse_mplib(loc: Union[str, Path]) -> ProjectInstance:
    """
    Parses a multi-project resource-constrained project scheduling problem
    instances from MPLIB.

    Parameters
    ----------
    loc
        The location of the instance.

    Returns
    -------
    Instance
        The parsed instance.
    """
    with open(loc, "r") as fh:
        lines = iter(line.strip() for line in fh.readlines() if line.strip())

    num_projects = int(next(lines))
    num_resources = int(next(lines))

    capacities = list(map(int, next(lines).split()))
    resources = [Resource(capacity=cap, renewable=True) for cap in capacities]

    projects: list[Project] = []
    activities: list[Activity] = []
    id2idx: dict[str, int] = {}  # maps activity names to idcs

    for project_idx in range(1, num_projects + 1):
        project_data = list(map(int, next(lines).split()))

        if len(project_data) == 3:
            # Modified MPLIB instances that include due date.
            num_activities, release_date, due_date = project_data
        else:
            # Original MPLIB instances do not include due date.
            num_activities, release_date = project_data
            due_date = None

        next(lines)  # denotes used resources, implies that demand > 0

        idcs = [len(activities) + idx for idx in range(num_activities)]
        projects.append(Project(idcs, release_date, due_date))

        for activity_idx in range(1, num_activities + 1):
            line = next(lines).split()
            idx = num_resources + 2
            duration, *demands, num_successors = list(map(int, line[:idx]))
            successors = line[idx:]
            assert len(successors) == num_successors

            mode = Mode(duration, demands)
            name = f"{project_idx}:{activity_idx}"  # original activity id
            id2idx[name] = len(activities)
            activities.append(Activity([mode], successors, [], name=name))  # type: ignore

    for activity in activities:
        # Map the successors ids from {project_idx:activity_idx}, to the
        # specific activitiy indices.
        idcs = [id2idx[succ] for succ in activity.successors]  # type: ignore
        activity.successors = idcs
        
    for activity in activities:
        # Map the predecessors ids to the
        # specific activitiy indices.
        for succ in activity.successors:
            activities[succ].predecessors.append(id2idx[activity.name])

    return ProjectInstance(resources, activities, projects)