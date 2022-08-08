import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    accessToken: null,
    refreshToken: null,
    isAuthenticated: false,
    isadmin: false,
  },
  getters: {
    isLoggedIn(state) {
      return state.isAuthenticated;
    },
    isAdmin(state) {
      return state.isadmin;
    }
  },
  mutations: {
    async isAdminMutation(state) {
      await axios
        .get("/api/v1/accounts/profile/is_admin/", {
          headers: {
            Authorization: `Bearer ${state.accessToken}`
          },
        })
        .then(response => {
          state.isadmin = response.data.isadmin
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    async refreshTokens(state) {
      var refreshToken = state.refreshToken;
      const formData = {
        refresh: refreshToken
      }
      await axios
        .post("/api/v1/auth/jwt/refresh", formData, {
          
        })
        .then(response => {
          var accessToken = response.data.access
          // Cookies.remove("accessToken")
          // Cookies.set("accessToken", accessToken)
          state.accessToken = accessToken
          state.refreshToken = refreshToken
          state.isAuthenticated = true
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    async verifyRefreshToken(state) {
      const formData = {
        token: state.refreshToken,
      }
      await axios
        .post("/api/v1/auth/jwt/verify", formData, {

        })
        .then(response => {
          if (Object.keys(response.data).length === 0) { // Если размер возвращаемых данных равен нулю, то токен действителен, обновляем access токен
            this.commit("refreshTokens")
          } else { // Если в возвращаемых данных есть хоть что-то, значит токен не действителен, удаляем все и просим пользователя пройти на страничку авторизации
            // Cookies.remove("accessToken")
            // Cookies.remove("refreshToken")

            state.accessToken = null;
            state.refreshToken = null;
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

      // Cookies.remove("accessToken")
      // Cookies.remove("refreshToken")

      // Cookies.set("accessToken", tokens.access)
      // Cookies.set("refreshToken", tokens.refresh)
    },
    removeTokens(state) {
      state.accessToken = null
      state.refreshToken = null
      state.isAuthenticated = false
      state.isadmin = false

      // Cookies.remove("accessToken")
      // Cookies.remove("refreshToken")
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