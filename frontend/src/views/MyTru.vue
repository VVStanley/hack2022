<template>
  <h1>Мои товары</h1>
  <table class="table table-striped table-hover">
    <thead>
    <tr>
      <th>ИД</th>
      <th>Наименование</th>
      <th>Категория</th>
      <th>Я продал</th>
      <th>Все продали</th>
      <th>Перспектива роста</th>
      <th>Всего покупают</th>
      <th>Динамика продаж</th>
      <th>Тренд</th>
    </tr>
    </thead>
    <tbody>
    <tr :key="index" v-for="(tru, index) in data.results">
      <td>{{ tru.id_cte }}</td>
      <td>{{ tru.cte_name }}</td>
      <td>{{ tru.category }}</td>
      <td>{{ tru.my_sum_amount }}</td>
      <td>{{ tru.sum_all }}</td>
      <td>{{ rounding(tru.growth_perspective, 0) }}%</td>
      <td>{{ tru.cons_cnt }}</td>
      <td width="100px">
        <ul>
          <li :key="index" v-for="(dynamic, index) in tru.dynamics">
            {{ dynamic.contract_year }}:&nbsp;{{ rounding(dynamic.amount) }}
          </li>
        </ul>
      </td>
      <td>
        <sparklines :indicatorStyles="indicatorStyles">
          <sparkline-curve :width="200"
                           :height="60"
                           :limit="0"
                           :refLineStyles="spRefLineStyles"
                           :styles="spCurveStyles"
                           :data="get_data_sparkline(tru.dynamics)"
                           />
        </sparklines>
      </td>
    </tr>
    </tbody>
  </table>
  <nav>
    <ul class="pagination">
      <li class="page-item">
        <a class="page-link" v-on:click.prevent="get_first" href="">Первая</a>
      </li>
      <li class="page-item" :class="[previous ? '' : 'disabled']">
        <a class="page-link" v-on:click.prevent="get_previous"
           :href="[previous ? previous : '#']">Назад</a>
      </li>
      <li class="page-item" :class="[next ? '' : 'disabled']">
        <a class="page-link" v-on:click.prevent="get_next"
           :href="[next ? next : '#']">Вперед</a>
      </li>
      <li class="page-item">
        <a class="page-link" v-on:click.prevent="get_last"
           href="#">Последняя</a>
      </li>
    </ul>
  </nav>
</template>

<script>
import {SparklineCurve, Sparklines} from 'vue-sparklines'

import axios from "@/axios";
import store from "@/store";

export default {
  name: "MyTru",
  components: {
    SparklineCurve,
    Sparklines
  },
  data() {
    return {
      spRefLineStyles: {
        stroke: '#d14',
        strokeOpacity: 5,
        strokeDasharray: '7, 7'
      },
      spCurveStyles: {
        stroke: '#dd2c00',
        fill: '#54a5ff',
        fontSize: '22'
      },
      data: [],
      limit: null,
      next: null,
      previous: null,
      count: 0,
      link: `/api/v1/tru/${store.getters.getUsername}/for-supplier/`
    }
  },
  mounted() {
    this.get_data()
  },
  methods: {
    get_data_sparkline(dynamics) {
      return dynamics.map(item => item.amount)
    },
    rounding(value, round = 2) {
      return parseInt(value).toFixed(round)
    },
    async get_last() {
      this.link = `/api/v1/tru/${store.getters.getUsername}/for-supplier/offset=${this.count - this.limit}`
      await this.get_data()
    },
    async get_first() {
      this.link = `/api/v1/tru/${store.getters.getUsername}/for-supplier/`
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