<template>
<h1>Мои данные</h1>
  <ul>
    <li v-if="supplier.sup_inn">ИНН: {{ supplier.sup_inn }}</li>
    <li v-if="supplier.sup_kpp">КПП: {{ supplier.sup_kpp }}</li>
    <li v-if="supplier.sup_name">Наименование: {{ supplier.sup_name }}</li>
    <li v-if="supplier.sup_type">Тип: {{ supplier.sup_type }}</li>
  </ul>
</template>

<script>
import axios from "@/axios/index";
import store from "@/store";

export default {
  name: "Suplier",
  data() {
    return {
      supplier: {
        sup_inn: null,
        sup_kpp: null,
        sup_name: null,
        sup_type: null,
      }
    }
  },
  mounted() {
    this.get_data()
  },
  methods: {
    async get_data() {
      await axios.get(
          `/api/v1/supplier/${store.getters.getUsername}`,
          {
            headers: {
              Authorization: 'Token ' + localStorage.getItem('authToken')

            }
          }
      ).then(
          ({data}) => this.supplier = data
      ).catch(
          error => console.log(error.response.data)
      )
    }
  }
}
</script>

