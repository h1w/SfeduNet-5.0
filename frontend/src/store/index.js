import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import Cookies from 'js-cookie'
import createPersistedState from 'vuex-persistedstate'

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
    async refreshTokens(state) {
      var refreshToken = this.$cookies.get("accessToken")
      if (refreshToken !== "null") {
        const formData = {
          refresh: refreshToken
        }
        await axios
          .post("/api/v1/auth/jwt/refresh", formData, {
            
          })
          .then(response => {
            var accessToken = response.data.access
            this.setAccessToken(accessToken)
            this.setRefreshToken(refreshToken)
            state.isAuthenticated = true
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })
      }
    },
    setUser(state, user) {
      state.user = user
    },
    setTokens(state, tokens) {
      state.accessToken = tokens.access
      state.refreshToken = tokens.refresh
      state.isAuthenticated = true

      Cookies.set("accessToken", tokens.access)
      Cookies.set("refreshToken", tokens.refresh)
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

      Cookies.remove("accessToken")
      Cookies.remove("refreshToken")
    },
  },
  actions: {
  },
  modules: {
  },
  plugins: [
    createPersistedState(),
  ],
})