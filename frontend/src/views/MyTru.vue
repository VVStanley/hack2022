<template>
<h1>MyTru</h1>
</template>

<script>
import axios from "@/axios";
import store from "@/store";

export default {
  name: "MyTru",
  data() {
    return {
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
          ({data})  => {
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