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
      changeData : function(data){

      }
    },
    watch: {
      checkData : function(data){
        const lineSeries = this.chart.addLineSeries();
        let datas = data
        lineSeries.setData(datas);

      }
    }
  }
</script>
