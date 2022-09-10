<template>
<h1>Мои данные</h1>
</template>

<script>
import axios from "@/axios/index";
import store from "@/store";

export default {
  name: "Suplier",
  mounted() {
    this.get_data()
  },
  methods: {
    async get_data() {
      console.log(store.state)
      console.log('us - ', store.getters.getUsername)
      await axios.get(
          '/api/v1/supplier/',
          {
            headers: {
              Authorization: 'Token ' + localStorage.getItem('authToken')

            }
          }
      ).then(
          // ({data}) => console.log(data)
      ).catch(
          // error => console.log(error.response.data)
      )
    }
  }
}
</script>

