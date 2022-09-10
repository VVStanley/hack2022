<template>
<h1>Клиенты</h1>
  <button v-on:click="show_top">Показать ТОП 7 клиентов</button>
  <div v-if="showTop">
    <input type="text" v-model="countCharts">
    <button v-on:click="update_chart">Обновить</button>
    <Doughnut
      :chart-options="chartOptions"
      :chart-data="chartData"
  />
  </div>
    <table class="table table-striped table-hover">
    <thead>
      <tr>
      <th>ИНН</th>
      <th>КПП</th>
      <th>Имя</th>
      <th>Сумма контрактов</th>
      </tr>
    </thead>
    <tbody>
    <tr :key="index" v-for="(consumer, index) in data.results">
      <td>{{consumer.cons_inn}}</td>
      <td>{{consumer.cons_kpp}}</td>
      <td>{{consumer.cons_name}}</td>
      <td>{{consumer.contract_sum}}</td>
    </tr>
    </tbody>
  </table>
  <nav>
  <ul class="pagination">
    <li class="page-item">
      <a class="page-link" v-on:click.prevent="get_first" href="">Первая</a>
    </li>
    <li class="page-item" :class="[previous ? '' : 'disabled']">
      <a class="page-link" v-on:click.prevent="get_previous" :href="[previous ? previous : '#']">Назад</a>
      </li>
    <li class="page-item" :class="[next ? '' : 'disabled']" >
      <a class="page-link" v-on:click.prevent="get_next" :href="[next ? next : '#']">Вперед</a>
  </li>
    <li class="page-item">
      <a class="page-link" v-on:click.prevent="get_last" href="#">Последняя</a>
    </li>
  </ul>
</nav>
</template>

<script>
import {Doughnut} from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from 'chart.js'
import axios from "@/axios";
import store from "@/store";

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

export default {
  name: "Consumers",
  components: { Doughnut },
  props: {
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 600
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      chartColors: [
          '#7CB9E8',
          '#C46210',
          '#3B7A57',
          '#9966CC',
          '#CD9575',
          '#3DDC84',
          '#A1CAF1',
          '#BFAFB2',
          '#7CB9E8',
          '#2E5894',
          '#660000',
          '#8A2BE2',
          '#79443B',
          '#D891EF',
          '#FFAA1D',
          '#A17A74',
          '#91A3B0',
          '#C19A6B',
          '#00CC99',
          '#D70040',
          '#56A0D3',
          '#ACE1AF',
          '#DE3163',
      ],
      data: [],
      limit: null,
      next: null,
      previous: null,
      count: 0,
      link: `/api/v1/consumers/?sup_username=${store.getters.getUsername}`,
      showTop: false,
      countCharts: 7,
      chartData: {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
      },
      chartOptions: {
        responsive: true
      }
    }
  },
  mounted() {
    this.get_data();
    this.get_data_to_chart(this.countCharts);
  },
  methods: {
    async get_data_to_chart(count) {
      await axios.get(
          `/api/v1/consumers/for-charts/?sup_username=${store.getters.getUsername}&count=${count}`,
          {
            headers: {
              Authorization: 'Token ' + localStorage.getItem('authToken')

            }
          }
      ).then(
          ({data}) => {
            console.log(data)
            let labels = data.map(item => item.cons_name)
            let myData = data.map(item => item.contract_sum)
            console.log(labels)
            console.log(myData)
            this.chartData = {

              labels: labels,
              datasets: [
                  {
                    backgroundColor: this.chartColors,
                data: myData
              }
              ]
            }
            console.log(this.chartData)
          }
      ).catch(
          error => console.log(error.response.data)
      )
    },
    update_chart() {
      this.get_data_to_chart(this.countCharts);
    },
    show_top() {
      this.showTop = !this.showTop
    },
    async get_last() {
      this.link = `/api/v1/consumers/?sup_username=${store.getters.getUsername}&offset=${this.count - this.limit}`
      await this.get_data()
    },
    async get_first() {
      this.link = `/api/v1/consumers/?sup_username=${store.getters.getUsername}`
      await this.get_data()
    },
    async get_previous() {
      this.link = this.previous
      await this.get_data()
    },
    async get_next() {
      this.link = this.next
      await this.get_data()
    },

    async get_data() {
      await axios.get(
          this.link,
          {
            headers: {
              Authorization: 'Token ' + localStorage.getItem('authToken')

            }
          }
      ).then(
          ({data}) => {
            console.log(data)
            this.next = data.next
            this.previous = data.previous
            this.count = data.count
            this.data = data

          }
      ).catch(
          error => console.log(error.response.data)
      )
    }
  }
}
</script>

<style scoped>

</style>