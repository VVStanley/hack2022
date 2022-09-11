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
      <td>{{ rounding(tru.my_sum_amount) }}</td>
      <td>{{ rounding(tru.sum_all) }}</td>
      <td>{{ rounding(tru.growth_perspective, 0) }}%</td>
      <td>
        {{ tru.cons_cnt }}
        <button class="btn btn-sm btn-success" v-on:click="openModal(tru)">
          Показать
        </button>
      </td>
      <td width="100px">
        <ul>
          <li :key="index" v-for="(dynamic, index) in tru.dynamics">
            г.{{ dynamic.contract_year }}:&nbsp;{{ rounding(dynamic.amount) }}
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

  <div :class="[showModal ? 'modal fade show ds' : 'modal fade dsn']"  aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header d-flex justify-content-center align-items-center">
        <figure>
            <blockquote class="blockquote">
              <h2>Заказчики которые покупают товар ИД:{{ truX.id_cte }}</h2>
            </blockquote>
            <figcaption class="blockquote-footer">
              {{ truX.cte_name }}
            </figcaption>
          </figure>

      </div>
      <div class="modal-body">
        <div class="d-flex justify-content-center align-items-center my-3">
      <table class="table table-striped table-hover">
          <thead>
          <tr>
            <th>ИД заказчика</th>
            <th>Количество</th>
            <th>Наименование</th>
            <th>Сумма</th>
            <th>Подписаться</th>
          </tr>
          </thead>
          <tbody>
            <tr :key="index" v-for="(consumer, index) in truXConsumersData">
              <td>{{consumer.id_consumer}}</td>
              <td>{{consumer.name}}</td>
              <td>{{consumer.quantity}}</td>
              <td>{{consumer.amount}}</td>
              <td>
                <button
                    type="button"
                    :class="[consumer.subscribe ? 'btn btn-success' : 'btn btn-primary']"
                    v-on:click="subscribe(consumer.uuid_id)"
                >
                  <span v-if="consumer.subscribe">Подписан</span>
                      <span v-else>Подписаться</span>
                </button>
              </td>
            </tr>
          </tbody>
      </table>

          </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" v-on:click="openModal"
                  data-mdb-dismiss="modal">Закрыть
          </button>

      </div>
    </div>
  </div>
</div>

  <div :class="[showSubscribeModal ? 'modal fade show ds' : 'modal fade dsn']" aria-labelledby="exampleModalLabel" aria-modal="true" role="dialog">
    <div class="modal-dialog modal-sm ptm">
      <div class="modal-content text-center">
        <div class="modal-header bg-success text-white d-flex justify-content-center">
          <h5 class="modal-title" id="exampleModalLabel">Вы подписаны</h5>
        </div>
        <div class="modal-body">
          <i class="fas fa-check fa-3x text-success"></i>
        </div>
        <div class="modal-footer d-flex justify-content-center">
          <button type="button" class="btn btn-outline-success" v-on:click="subscribe" data-mdb-dismiss="modal">
            Отлично!
          </button>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import {SparklineCurve, Sparklines} from 'vue-sparklines'
import { v4 as uuidv4 } from 'uuid';
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
      truX: {
        id_cte: null,
        cte_name: null
      },
      truXConsumersData: [],
      showModal: false,
      showSubscribeModal: false,
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
    subscribe(uuid_id) {
      this.showSubscribeModal = !this.showSubscribeModal;
      this.truXConsumersData.forEach(item => {
        if (item.uuid_id === uuid_id) {
          item.subscribe = true
        }
      })
    },
    async openModal(tru) {
      this.truX = tru;
      await this.get_data_truX()
      this.showModal = !this.showModal
    },
    async get_data_truX() {
      await axios.get(
          `/api/v1/consumers/${this.truX.id_cte}/all_sale/`,
          {
            headers: {
              Authorization: 'Token ' + localStorage.getItem('authToken')

            }
          }
      ).then(
          ({data}) => {
            this.truXConsumersData = data;
            this.truXConsumersData.map(item => {
              item['uuid_id'] = uuidv4();
              item['subscribe'] = false;
            })
            console.log(this.truXConsumersData)
          }
      ).catch(
          error => console.log(error.response.data)
      )
    },
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
.ds {
  display: block;
}

.dsn {
  display: none;
}
.modal-xl {
    max-width: 90%;
}
.ptm{
  padding-top: 120px;
}
.blockquote-footer {
    margin-top: -1rem;
    margin-bottom: 1rem;
    font-size: 1em;
    color: #757575;
}
</style>