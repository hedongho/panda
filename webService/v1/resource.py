
import v1.ctrl.dashboardCtrl as systemCtrl

API_ROOT = "/v1/monitor"

api_resource = {
    systemCtrl.QuickEntry: API_ROOT+"/dashboard/quickentry",
    systemCtrl.System: API_ROOT+"/dashboard/system"
}