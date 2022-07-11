import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    accessToken: null,
    refreshToken: null,
    isAuthenticated: false,
  },
  getters: {
    isLoggedIn(state) {
      return state.isAuthenticated;
    },
  },
  mutations: {
    async refreshAccessToken(state) {
      const formData = {
        refresh: this.refreshToken
      }
      await axios
        .post("/api/v1/auth/jwt/refresh", formData, {
          
        })
        .then(response => {
          var accessToken = response.data.access
          this.setAccessToken(accessToken)
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    setUser(state, user) {
      state.user = user
    },
    setTokens(state, accessToken, refreshToken) {
      state.accessToken = accessToken
      state.refreshToken = refreshToken
      state.isAuthenticated = true
      // this.$cookies.set("accessToken", accessToken, "1d")
      // this.$cookies.set("refreshToken", refreshToken, "14d")
      // console.log(this.$cookies.get('user').name)
    },
    setAccessToken(state, accessToken) {
      state.accessToken = accessToken
    },
    setRefreshToken(state, refreshToken) {
      state.refreshToken = refreshToken
    },
    removeTokens(state) {
      state.accessToken = null
      state.refreshToken = null
      state.isAuthenticated = false
    },
  },
  actions: {
  },
  modules: {
  }
})