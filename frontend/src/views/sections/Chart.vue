<template>
  <v-container>
    <v-btn @click="changeData">Change Data</v-btn>
    <test-chart v-bind:chartdata="chartdata"></test-chart>
  </v-container>
</template>

<script>
  import TestChart from '@/components/chart/TestChart'

  export default {
    name: 'Chart',
    data :function() {
      return { 
        chartdata: 
          [ { time: '2019-04-11', value: 80.01 },
            { time: '2019-04-12', value: 96.63 },
            { time: '2019-04-13', value: 76.64 },
            { time: '2019-04-14', value: 81.89 },
            { time: '2019-04-15', value: 74.43 },
            { time: '2019-04-16', value: 80.01 },
            { time: '2019-04-17', value: 96.63 },
            { time: '2019-04-18', value: 76.64 },
            { time: '2019-04-19', value: 81.89 },
            { time: '2019-04-20', value: 74.43 }]
        
      }
    },
    components:{
      TestChart:TestChart
    },
    mounted : function() {
    },
    methods: {
      changeData : function(){
        this.chartdata = 
          [ { time: '2019-04-11', value: 90.01 },
            { time: '2019-04-12', value: 56.63 },
            { time: '2019-04-13', value: 76.64 },
            { time: '2019-04-14', value: 41.89 },
            { time: '2019-04-15', value: 54.43 },
            { time: '2019-04-16', value: 30.01 },
            { time: '2019-04-17', value: 56.63 },
            { time: '2019-04-18', value: 46.64 },
            { time: '2019-04-19', value: 71.89 },
            { time: '2019-04-20', value: 94.43 }]
      }
    },
  }
</script>
