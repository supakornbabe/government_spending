document.addEventListener('DOMContentLoaded', function() {
    Highcharts.chart('budgetAndUsage', {

        title : {
            /* Solar Employment Growth by Sector */
            text : 'Budget and money usage of Ministry of Interior, 2005-2019'
        },

        subtitle : {
            text :
                'Source: dataservices.mof.go.th/Dataservices/GovernmentExpenditureEconomyMinistry'
        },

        yAxis : {title : {text : 'Million THB'}},

        legend :
            {layout : 'vertical', align : 'right', verticalAlign : 'middle'},

        xAxis : {title : {text : 'Year'}},

        plotOptions :
            {series : {label : {connectorAllowed : 0}, pointStart : 2005}},

        series : [
            {
                name : 'Use',
                data : [
                    127741.379, 143661.092, 161822.787, 190930.145, 177786.968,
                    174755.746, 213812.275, 250224.166, 266306.374, 280412.117,
                    316307.295, 319395.893, 313283.846, 350983.047, 249744.861
                ]
            },
            {
                name : 'Budget',
                data : [
                    139800.179, 160643.476, 179115.753, 190930.145, 207826.344,
                    187998.707, 239479.125, 285254.857, 308835.034, 333145.15,
                    340171.626, 341820.817, 335145.525, 386179.349, 371801.731
                ]

            }
        ],

        responsive : {
            rules : [ {
                condition : {maxWidth : 500},
                chartOptions : {
                    legend : {
                        layout : 'horizontal',
                        align : 'center',
                        verticalAlign : 'bottom'
                    }
                }
            } ]
        }

    });
})