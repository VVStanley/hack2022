<template>
<h1>Мои контракты</h1>
  <table class="table table-striped table-hover">
    <thead>
      <tr>
      <th>ИД контракта</th>
      <th>Контракт</th>
      <th>Клиент</th>
      <th>Дата публикации</th>
      <th>Дата контракта</th>
      <th>Цена</th>
      <th>Элементы контракта</th>
      </tr>
    </thead>
    <tbody>
    <tr :key="index" v-for="(contract, index) in data.results">
      <td>{{contract.id_contract}}</td>
      <td>{{contract.contract}}</td>
      <td>
        {{contract.consumer.cons_inn}}/{{contract.consumer.cons_kpp}} <br> {{contract.consumer.cons_name}}
      </td>
      <td>{{contract.pub_date}}</td>
      <td>{{contract.contract_date}}</td>
      <td>{{contract.contract_price}}</td>
      <td width="30%">
        <ul>
          <li :key="index" v-for="(element, index) in contract.elements">
            <span v-if="element.id_element">ИД: {{element.id_element}}</span>
            <span v-else class="text-danger">Неизвестно</span>
            Кол-во: {{element.quantity}}
            Сумма: {{element.amount}}
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
import store from "@/store";

export default {
  name: "Contracts",
  data() {
    return {
      data: [],
      limit: null,
      next: null,
      previous: null,
      count: 0,
      link: `/api/v1/contracts/?sup_username=${store.getters.getUsername}`
      // link: `/api/v1/contracts/?sup_username=9718042934771301001`
    }
  },
  mounted() {
    this.get_data()
  },
  methods: {
    async get_last() {
      this.link = `/api/v1/contracts/?sup_username=${store.getters.getUsername}&offset=${this.count - this.limit}`
      await this.get_data()
    },
    async get_first() {
      this.link = `/api/v1/contracts/?sup_username=${store.getters.getUsername}`
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