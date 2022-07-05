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
      return state.isAuthenticated
    },
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    setTokens(state, accessToken, refreshToken) {
      this.setAccessToken(accessToken)
      this.setRefreshToken(refreshToken)
      this.isAuthenticated = true
      
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