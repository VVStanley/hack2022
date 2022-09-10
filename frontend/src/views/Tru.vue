<template>
<h1>Стандартная товарная еденица</h1>
  <table class="table table-striped table-hover">
    <thead>
      <tr>
        <th>ИД</th>
        <th>Наименование</th>
      <th>Категория</th>
      <th>КПГЗ</th>
      <th>Характеристики</th>
      </tr>
    </thead>
    <tbody>
      <tr :key="index" v-for="(item, index) in data.results">
        <td>{{ item.id_cte }}</td>
        <td>{{ item.cte_name }}</td>
        <td>{{ item.category }}</td>
        <td>{{ item.kpgz_code }}</td>
        <td>
          <ul>
            <li :key="index" v-for="(property, index) in item.properties">
              {{ property.prop_name }}: {{ property.prop_value }} {{property.prop_unit ? 'ЕД.ИЗМ:' + property.prop_unit : ''}}
            </li>
          </ul>
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
import axios from "@/axios/index";

export default {
  name: "Tru",
  data() {
    return {
      data: [],
      limit: null,
      next: null,
      previous: null,
      count: 0,
      link: '/api/v1/tru/'
    }
  },
  mounted() {
    this.get_data()
  },
  methods: {
    async get_last() {
      this.link = `/api/v1/tru/?offset=${this.count - this.limit}`
      await this.get_data()
    },
    async get_first() {
      this.link = '/api/v1/tru/'
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
          ({data})  => {
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