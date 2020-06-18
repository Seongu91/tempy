<template>
  <v-container>

    <v-col cols="12" sm="6" md="4">
      <v-menu
        v-model="startDateMenu"
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        full-width
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="startDate"
            label="Start"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker v-model="startDate" @input="startDateMenu = false" :show-current="false"></v-date-picker>
      </v-menu>
    </v-col>

    <v-col cols="12" sm="6" md="4">
      <v-menu
        v-model="endDateMenu"
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        full-width
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="endDate"
            label="End"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker v-model="endDate" @input="endDateMenu = false" :show-current="false"></v-date-picker>
      </v-menu>
    </v-col>

    <v-btn @click="changeData">Change Data</v-btn>
    <v-btn @click="getData">Get Data</v-btn>
    <test-chart v-bind:chartdata="chartdata"></test-chart>
  </v-container>
</template>

<script>
  import axios from 'axios';
  import TestChart from '@/components/chart/TestChart'

  export default {
    name: 'Chart',
    data :function() {
      return { 
        startDateMenu : false,
        startDate : new Date('2020-03-01').toISOString().substr(0, 10),
        endDateMenu : false,
        endDate : new Date().toISOString().substr(0, 10),
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
      },
      getData : function(){
        axios({
                method: 'GET',
                url : '/getdata',
                params : {
                  startDate : this.startDate,
                  endDate : this.endDate
                }
              }).then((response) => {
                console.log(response);
                response.data.forEach(element => {
                  element['time'] = element['date']
                  delete element["date"];
                  element['value'] = element['closing']
                  delete element["closing"];
                });
                this.chartdata =  response.data;
                
              }).catch((ex)=> {
                console.log("ERR!!!!! : ", ex)
              })
      }
    },
  }
</script>
