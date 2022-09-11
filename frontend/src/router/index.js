import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login'
import Tru from '../views/Tru'
import Logout from '../views/Logout'
import store from "@/store";
import Supplier from '../views/Suplier'
import Contracts from '../views/Contracts'
import Consumers from '../views/Consumers'
import MyTru from '../views/MyTru'

const routes = [
  {
    path: '/',
    name: 'home',
    meta: {
      needAuth: false,
    },
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    meta: {
      needAuth: false,
    },
    component: Login
  },
  {
    path: '/logout',
    name: 'logout',
    meta: {
      needAuth: true,
    },
    component: Logout
  },
  {
    path: '/tru',
    name: 'tru',
    meta: {
      needAuth: true,
    },
    component: Tru
  },
  {
    path: '/mytru',
    name: 'mytru',
    meta: {
      needAuth: true,
    },
    component: MyTru
  },
  {
    path: '/supplier',
    name: 'supplier',
    meta: {
      needAuth: true,
    },
    component: Supplier
  },
  {
    path: '/contracts',
    name: 'contracts',
    meta: {
      needAuth: true,
    },
    component: Contracts
  },

  {
    path: '/consumers',
    name: 'consumers',
    meta: {
      needAuth: true,
    },
    component: Consumers
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(
  async (to, from, next) => {
    let needAuth = to.matched.some(route => route.meta.needAuth)
    let isAuth = store.getters.isAuth

    console.log('needAuth', needAuth)
    console.log('isAuth', isAuth)

    if (needAuth && !isAuth) {
      next({name: 'login'})
    } else {
      if (!needAuth && isAuth) {
        next({name: 'supplier'})
      }
      next()
    }
  }
)


export default router
