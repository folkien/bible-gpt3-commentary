'''
Created on 3 gru 2020

@author: spasz
'''
from datetime import datetime
from subprocess import check_output

# Default subprocess calls timeout
defaultTimeout = 10
# Default result if exception
defaultResult = 'Unknown'


def GetGitTag() -> str:
    '''Return current git revision.'''
    try:
        return check_output(['git', 'describe', '--tags', '--abbrev=0'], timeout=defaultTimeout).strip().decode('utf-8')
    except:
        return defaultResult


def GetGitRev() -> str:
    '''Return current git revision.'''
    try:
        return check_output(['git', 'describe', '--tags'], timeout=defaultTimeout).strip().decode('utf-8')
    except:
        return defaultResult


def GetGitBranchRev() -> str:
    '''
        Return current git revision with branch name.
        - fix for branches with slash/backslash
    '''
    try:
        branchName = check_output(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'], timeout=defaultTimeout).strip().decode('utf-8')
        branchName = branchName.replace('/', '.').replace('\\', '.')
        return GetGitRev() + '-' + branchName
    except:
        return defaultResult


def GetYearWeekRev() -> str:
    '''Return current YearWeek revision - ubuntu schema.'''
    now = datetime.now()
    return now.strftime('%y%Vv%w')


def GetYearWeekTimeRev() -> str:
    '''Return current YearWeek revision - ubuntu schema.'''
    now = datetime.now()
    return now.strftime('%y%Vv%w. %H:%M:%S')
