var xhr = new XMLHttpRequest(),
method = "GET",
url = "https://api.nodal.direct/v1/index.php/api/getDynamicPriceData";
xhr.open(method, url, true);
xhr.send();
	
window.onload = function () {

	xhr.onreadystatechange = function () {

		if (xhr.readyState === 4 && xhr.status === 200) {

			var dlf_price_index_array = [];
    		var cyber_price_index_array = [];
			var huda_price_index_array = [];
	
			var api_data = xhr.responseText;
			var api_json = JSON.parse(api_data); 
			var data = api_json["data"];

			for(var i=0; i<data.length; i++) {
			
                iter_data = data[i];
                dp_price_index = iter_data["dp_price_index"];
                dcc_price_index = iter_data["dcc_price_index"];
                hcc_price_index = iter_data["hcc_price_index"];
				dp_date = iter_data["date"];
			
				var datearray = dp_date.split("-");
				var newdate = datearray[0] + ', ' + datearray[1] + ', ' + datearray[2];
			
                dlf_price_index_array.push({x:new Date(newdate), y:Number(dp_price_index)});
                cyber_price_index_array.push({x:new Date(newdate), y:Number(dcc_price_index)});
                huda_price_index_array.push({x:new Date(newdate), y:Number(hcc_price_index)});   
			}

			var chart = new CanvasJS.Chart("chartContainer", {
				title: {
					text: "Market Inflation Analysis"
				},
				axisX: {
					valueFormatString: "YYYY MM DD"
				},
				axisY2: {
					title: "Price Index",
					prefix: " ",
					suffix: "%"
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
						name: "Arbor(Golf Course Road[Price Index])",
						showInLegend: true,
						markerSize: 1,
    			    	yValueFormatString: "₹#,###",
						dataPoints: dlf_price_index_array
					},
                    {
						type:"line",
						axisYType: "secondary",
						name: "Arbor(Cyber City[Price Index])",
						showInLegend: true,
						markerSize: 1,
    			    	yValueFormatString: "₹#,###",
						dataPoints: cyber_price_index_array
					},
                    {
						type:"line",
						axisYType: "secondary",
						name: "Arbor(Suites[Price Index])",
						showInLegend: true,
						markerSize: 1,
    			    	yValueFormatString: "₹#,###",
						dataPoints: huda_price_index_array
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

		else {
			console.log("nothing happened")
		}
	}	
};