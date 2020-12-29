app.controller('cntrl_3', function ($scope, $rootScope, $timeout) {


    $scope.$on('enable_Btns', function (event, data) {

        $scope.MiniMenuData = [{
            "FunctionName": "FavouriteFunction",
            "FunctionIcon": "",
            "FunctionValue": "FavouriteValue"
        }, {
            "FunctionName": "LameFunction",
            "FunctionIcon": "",
            "FunctionValue": "LameValue"
        }
        ];

        console.log(data.btnEnable);
        $rootScope.btn_status = data.btnEnable;
        $rootScope.btn_status_msg = data.message;
        $timeout(function () {
            $scope.$emit('btn_enabled', { "main_ctrl_msg": "yes I enabled it" });
        }, 1000)
    });
});