<template>
  <div id="test-chart"></div>
</template>

<script>
  import { createChart } from 'lightweight-charts';

  export default {
    name: 'TestChart',
    data :function() {
      return { 
        chart:''
      }
    },
    props: ['chartdata'],
    mounted:function(){
      this.chart = createChart(document.getElementById('test-chart'), { width: 400, height: 300 });
      const lineSeries = this.chart.addLineSeries();
      let data = this.chartdata
      lineSeries.setData(data);
    },
    methods:{
      addData : function(data){
        const lineSeries = this.chart.addLineSeries();
        lineSeries.setData(data);
      }
    },
    watch: {
      chartdata : function(data){
        this.addData(data);
      }
    }
  }
</script>
