// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: marker2.labels,
    datasets: [{
      label: "확진자수 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(255, 140, 0, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: marker2.data,
    },{
      label: "사망자수 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(255, 45, 45, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: marker2.data2,
    },{
      label: "완치자수 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(100, 205, 205, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: marker2.data3,
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return '' + number_format(value);
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + '' + number_format(tooltipItem.yLabel);
        }
      }
    }
  }
});

// Area Chart Example2
var ctx_two = document.getElementById("myAreaChart_two");
var myLineChart = new Chart(ctx_two, {
  type: 'line',
  data: {
    labels: ["19년11월", "19년12월", "20년1월"],
    datasets: [{
      label: "입도 현황(명) ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(111, 111, 111, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(100, 115, 223, 1)",
      pointBorderColor: "rgba(111, 111, 111, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [100266, 98541, 89678],
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return '' + number_format(value);
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + '' + number_format(tooltipItem.yLabel);
        }
      }
    }
  }
});

// 입도객현황
var ctx_three = document.getElementById("myAreaChart_three");
var myLineChart = new Chart(ctx_three, {
  type: 'line',
  data: {
    labels: 입도객현황.날짜,
    datasets: [{
      label: "내국인 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(255, 140, 0, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: 입도객현황.내국인,
    },{
      label: "외국인 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(255, 140, 0, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: 입도객현황.외국인,
    },{
      label: "중국인 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(255, 140, 0, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: 입도객현황.중국인,
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return '' + number_format(value);
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + '' + number_format(tooltipItem.yLabel);
        }
      }
    }
  }
});


// 한국 증가추이
var 분석차트_한국누적확진자_날짜_Array = [];
var 분석차트_한국누적확진자_확진자_Array = [];
var 분석차트_한국누적확진자_전일차_Array = [];
var 분석차트_한국누적확진자_사망자_Array = [];

for (var i = 0; i < 분석차트_한국누적확진자.length; i++) {
  분석차트_한국누적확진자_날짜_Array.push(분석차트_한국누적확진자[i][0]);
  분석차트_한국누적확진자_확진자_Array.push(분석차트_한국누적확진자[i][1]);
  분석차트_한국누적확진자_전일차_Array.push(분석차트_한국누적확진자[i][2]);
  분석차트_한국누적확진자_사망자_Array.push(분석차트_한국누적확진자[i][3]);
}

// console.log(분석차트_한국누적확진자_날짜_Array);
// console.log(분석차트_한국누적확진자_확진자_Array);
// console.log(분석차트_한국누적확진자_전일차_Array);
// console.log(분석차트_한국누적확진자_사망자_Array);


// 한국 누적 확진자 그래프
var ctx_four = document.getElementById("myAreaChart_four");
var myLineChart = new Chart(ctx_four, {
  type: 'line',
  data: {
    labels: 분석차트_한국누적확진자_날짜_Array,
    datasets: [{
      label: "한국 확진자 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(255, 140, 0, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: 분석차트_한국누적확진자_확진자_Array,
    },{
      label: "전일대비 증가 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(100, 205, 205, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: 분석차트_한국누적확진자_전일차_Array,
    },{
      label: "사망자 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(255, 45, 45, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: 분석차트_한국누적확진자_사망자_Array,
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 5
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return '' + number_format(value);
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + '' + number_format(tooltipItem.yLabel);
        }
      }
    }
  }
});




//확진자 추이(한국_세계)
var 확진자추이그래프_date = [];

var 확진자추이그래프_세계확진자 = [];
var 확진자추이그래프_세계확진자편차 = [];
var 확진자추이그래프_세계비율 = [];

var 확진자추이그래프_한국확진자 = [];
var 확진자추이그래프_한국확진자편차 = [];
var 확진자추이그래프_한국비율 = [];

for (let i = 0; i < 분석차트_한국누적확진자.length; i++){
  확진자추이그래프_date.push(분석차트_한국누적확진자[i][0]);
  확진자추이그래프_한국확진자.push(분석차트_한국누적확진자[i][1]);
  확진자추이그래프_한국확진자편차.push(분석차트_한국누적확진자[i][2]);
  확진자추이그래프_한국비율.push((확진자추이그래프_한국확진자편차[i]/확진자추이그래프_한국확진자[i])*100)
}

// console.log("test", marker2.labels.indexOf("2/1"))

for (let i = marker2.labels.indexOf("2/1"); i < marker2.labels.length; i++){
  확진자추이그래프_세계확진자.push(parseInt(marker2.data[i], 10));
  if (marker2.data[i] - marker2.data[i-1] < 0){
    확진자추이그래프_세계확진자편차.push(0);
  } else{
    확진자추이그래프_세계확진자편차.push(parseInt(marker2.data[i] - marker2.data[i-1], 10));
  }
}

for (let i = 0; i < 확진자추이그래프_세계확진자.length; i++){
  확진자추이그래프_세계비율.push((확진자추이그래프_세계확진자편차[i]/확진자추이그래프_세계확진자[i])*100);
}

var ctx_five = document.getElementById("myAreaChart_five");
var myLineChart = new Chart(ctx_five, {
  type: 'line',
  data: {
    labels: 확진자추이그래프_date,
    datasets: [{
      label: "한국 추이 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(255, 140, 0, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: 확진자추이그래프_한국비율,
    },{
      label: "세계 추이 ",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(100, 205, 205, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 115, 223, 1)",
      pointBorderColor: "rgba(155, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: 확진자추이그래프_세계비율,
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 5
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return '' + number_format(value);
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + '' + number_format(tooltipItem.yLabel) + '%';
        }
      }
    }
  }
});


var 한국누적_확진 = [];
var 한국누적_날짜 = [];

for (var i = 0; i < 분석차트_한국누적확진자.length; i++) {
  한국누적_날짜.push(분석차트_한국누적확진자[i][0]);
  한국누적_확진.push(분석차트_한국누적확진자[i][1]);
}

var ctx_six = document.getElementById("myAreaChart_six");
var myChart = new Chart(ctx_six, {
  type: "line",
  data: {
    labels: 한국누적_날짜,
    datasets: [
      {
        label: "한국 누적 확진자",
        borderColor: ["rgba(255, 99, 132, 1)"],
        data: 한국누적_확진
      }
    ]
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 5
      }
    },
    scales: {
      yAxes: [
        {
          type: "logarithmic",
          ticks: {
            min: 10,
            max: 100000,
            callback: function(value, index, values) {
              if (value === 1000000) return "1M";
              if (value === 100000) return "100K";
              if (value === 10000) return "10K";
              if (value === 1000) return "1K";
              if (value === 100) return "100";
              if (value === 10) return "10";
              if (value === 0) return "0";
              return null;
            }
          }
        }
      ]
    }
  }
});
