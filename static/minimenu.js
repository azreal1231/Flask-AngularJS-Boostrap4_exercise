app.controller('minimenu_cntrl',function($scope , $rootScope)
{
    $scope.MiniMenuData = [];
    
    $scope.$on('populateMiniMenu',function(event, data)
    {
        // console.log(event);
        // console.log(data);
        $scope.MiniMenuData = data;
    });


    $scope.MiniMenuFunctions = function(_command)
    {
        $scope.$emit('fromMiniMenu', _command);
        alert(_command);
    }
});