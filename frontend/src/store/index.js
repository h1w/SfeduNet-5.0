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
      var refreshToken = Cookies.get("refreshToken")
      const formData = {
        refresh: refreshToken
      }
      await axios
        .post("/api/v1/auth/jwt/refresh", formData, {
          
        })
        .then(response => {
          var accessToken = response.data.access
          Cookies.remove("accessToken")
          Cookies.set("accessToken", accessToken)
          this.setAccessToken(accessToken)
          this.setRefreshToken(refreshToken)
          state.isAuthenticated = true
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    async verifyRefreshToken(state) {
      const formData = {
        token: Cookies.get("refreshToken"),
      }
      await axios
        .post("/api/v1/auth/jwt/verify", formData, {

        })
        .then(response => {
          if (Object.keys(response.data).length === 0) { // Если размер возвращаемых данных равен нулю, то токен действителен, обновляем access токен
            this.commit("refreshTokens")
          } else { // Если в возвращаемых данных есть хоть что-то, значит токен не действителен, удаляем все и просим пользователя пройти на страничку авторизации
            Cookies.remove("accessToken")
            Cookies.remove("refreshToken")

    
            state.isAuthenticated = false;
          }
        })
    },
    setUser(state, user) {
      state.user = user
    },
    setTokens(state, tokens) {
      state.accessToken = tokens.access
      state.refreshToken = tokens.refresh
      state.isAuthenticated = true

      Cookies.remove("accessToken")
      Cookies.remove("refreshToken")

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