import tracLib

#if you defined your own types you should add them to the map
TYPES = {
    "defect"        :   "Bug",
    "enhancement"   :   "Feature",
    "task"          :   "Task",
}

#if you defined your own priorities you should add them to the map
PRIORITIES = {
    "lowest"       :   "Minor",        #Minor
    "low"         :   "Normal",        #Normal
    "normal"         :   "Major",        #Major
    "high"      :   "Critical",        #Critical
    "highest"       :   "Show-stopper"         #Show-stopper
}
#we convert resolutions and statuses into statuses
RESOLUTIONS = {
    "duplicate"     :   "Duplicate",
    "fixed"         :   "Fixed",
    "wontfix"       :   "Won't fix",
    "worksforme"    :   "Can't Reproduce",
    "invalid"       :   "Can't Reproduce"
    #   :   "To be discussed
}

STATES = {
    "accepted"      :   "Submitted",
    "new"           :   "Open",
    "reopened"      :   "Reopened",
    "assigned"      :   "Submitted",
    "testing"       :   "Fixed",
    "closed"        :   "Verified"
}

# if you don't change rules of importing, don't change this map
tracLib.CUSTOM_FIELD_TYPES = {
    "text"          :   "string",
    "checkbox"      :   "enum[*]",
    "select"        :   "enum[1]",
    "radio"         :   "enum[1]",
    "textarea"     :   "string"
}

tracLib.FIELD_VALUES = {
    "Priority"      :   PRIORITIES,
    "Type"          :   TYPES,
    "State"         :   dict(RESOLUTIONS.items() + STATES.items())
}

tracLib.FIELD_TYPES = {
    "Priority"          :   "enum[1]",
    "Type"              :   "enum[1]",
    "State"             :   "state[1]",
    "Fix versions"      :   "version[*]",
    "Affected versions" :   "version[*]",
    "Assignee"          :   "user[1]",
    "Severity"          :   "enum[1]",
    "Subsystem"         :   "ownedField[1]"
}

tracLib.FIELD_NAMES = {
    "Resolution"        :   "State",
    "Status"            :   "State",
    "Owner"             :   "Assignee",
    "Version"           :   "Affected versions",
    "Milestone"         :   "Fix versions",
    "Component"         :   "Subsystem"
}


# the default email to register users who doesn't have one
tracLib.DEFAULT_EMAIL = "user@server.com"
# if true users who were not authorized are registered
# else they are known as guests
tracLib.ACCEPT_NON_AUTHORISED_USERS = False

# Enable support for plugins to import timetracking data into YouTrack.
# You can set this option manualy if autodetection doesn't work correctly.
# Available options:
#   - trachours
#   - timingandestimationplugin
tracLib.SUPPORT_TIME_TRACKING = "auto"