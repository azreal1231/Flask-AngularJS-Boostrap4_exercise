app.controller('graphCtrl', function ($scope, $rootScope) {

    $scope.massPopChart = null;

    $rootScope.$on('populate_graph', function (event, data) {
        labels = [];
        values = [];
        for (dicKey in data) {
            labels.push(dicKey)
            values.push(data[dicKey])
        }

        console.log("Labels: " + labels);
        console.log("values: " + values);      
        
        let myChart = document.getElementById('myChart').getContext('2d');

        // Global Options
        Chart.defaults.global.defaultFontFamily = 'Lato';
        Chart.defaults.global.defaultFontSize = 18;
        Chart.defaults.global.defaultFontColor = '#777';

        try{
            $scope.massPopChart.destroy();
        } catch {
            console.log("Chart destroy exception caught. There was no chart.");
        }
        
        $scope.massPopChart = new Chart(myChart, {
            type: 'bar', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
            data: {
                labels: labels,
                datasets: [{
                    label: 'Population',
                    data: values,
                    //backgroundColor:'green',
                    backgroundColor: 'green',
                    borderWidth: 1,
                    borderColor: '#777',
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000'
                }]
            },
            options: {
                title: {
                    display: true,
                    text: 'Largest Cities In Massachusetts',
                    fontSize: 25
                },
                legend: {
                    display: true,
                    position: 'right',
                    labels: {
                        fontColor: '#000'
                    }
                },
                layout: {
                    padding: {
                        left: 50,
                        right: 0,
                        bottom: 0,
                        top: 0
                    }
                },
                tooltips: {
                    enabled: true
                }
            }
        });
    })

});