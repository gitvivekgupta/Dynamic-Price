var xhr = new XMLHttpRequest(),
method = "GET",
url = "https://api.nodal.direct/v1/index.php/api/getDynamicPriceData";
xhr.open(method, url, true);
xhr.send();
	
window.onload = function () {

	xhr.onreadystatechange = function () {

		if (xhr.readyState === 4 && xhr.status === 200) {

			var dp_median, dcc_median, hcc_median;
    		var dlf_data_array = [];
    		var cyber_data_array = [];
    		var huda_data_array = [];

			var api_data = xhr.responseText;
			var api_json = JSON.parse(api_data); 
            var data = api_json["data"];

			for(var i=0; i<data.length; i++) {
			
                iter_data = data[i];
                dp_median = iter_data["dp_median_price"];
                dp_median = Math.ceil(dp_median);
                dcc_median = iter_data["dcc_median_price"];
                dcc_median = Math.ceil(dcc_median);
                hcc_median = iter_data["hcc_median_price"];
                hcc_median = Math.ceil(hcc_median);
				dp_date = iter_data["date"];
			
				var datearray = dp_date.split("-");
				var newdate = datearray[0] + ', ' + datearray[1] + ', ' + datearray[2];
			
                dlf_data_array.push({x:new Date(newdate), y:Number(dp_median)});
                cyber_data_array.push({x:new Date(newdate), y:Number(dcc_median)});
                huda_data_array.push({x:new Date(newdate), y:Number(hcc_median)});  
            }

			var chart = new CanvasJS.Chart("chartContainer", {
				title: {
					text: "OYO Market Price Analysis"
				},
				axisX: {
					valueFormatString: "YYYY MM DD"
				},
				axisY2: {
					title: "Median Price",
					prefix: "Rs. ",
					suffix: " "
				},
				toolTip: {
					shared: true
				},
				legend: {
					cursor: "pointer",
					verticalAlign: "top",
					horizontalAlign: "center",
					dockInsidePlotArea: true,
					itemclick: toogleDataSeries
				},
				data:[
					{
						type:"line",
						axisYType: "secondary",
						name: "Arbor(Golf Course Road)",
						showInLegend: true,
						markerSize: 1,
    			    	yValueFormatString: "#,###",
						dataPoints: dlf_data_array
                    },
					{
						type:"line",
						axisYType: "secondary",
						name: "Arbor(Cyber City)",
						showInLegend: true,
						markerSize: 1,
    			    	yValueFormatString: "#,###",
						dataPoints: cyber_data_array
                    },
					{
						type:"line",
						axisYType: "secondary",
						name: "Arbor(Suites)",
						showInLegend: true,
						markerSize: 1,
    			    	yValueFormatString: "#,###",
						dataPoints: huda_data_array
                    }
				]
			});

			chart.render();

			function toogleDataSeries(e){
				if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
					e.dataSeries.visible = false;
				} else{
					e.dataSeries.visible = true;
				}
				chart.render();
			}
		}	
	}	
};