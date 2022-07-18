<template>
  <div>
    <b-navbar variant="faded" toggleable="lg">
      <b-navbar-brand :to="{name: 'map'}">
        <img id="navbar-brand-logo" :src="logoSVG">
        Амброзия
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item :to="{name: 'map'}">Карта</b-nav-item>
          <b-nav-item :to="{name: 'instruction'}">Приложение</b-nav-item>
          <b-nav-item :to="{name: 'volunteering'}">Волонтерство</b-nav-item>
          <b-nav-item :to="{name: 'about'}">О Нас</b-nav-item>
          <b-nav-item :to="{name: 'contacts'}">Контакты</b-nav-item>
          <!-- <b-nav-item href="https://tagproject-api.sfedu.ru/api/v1/map/markers/export_csv" target="_blank">Экспорт CSV</b-nav-item> -->
          <b-nav-item v-if="isLoggedIn" @click="exportCSVFunction()">Экспорт CSV</b-nav-item>
          <b-nav-item v-if="!isLoggedIn" :to="{name: 'LogIn'}">Войти</b-nav-item>
          <b-nav-item v-if="isLoggedIn" @click="logout()"><img id="navbar-account-logout-icon" :src="logoutSVG"></b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
import axios from 'axios';
import { saveAs } from 'file-saver';

export default {
  name: 'Navbar',
  data: function () {
    return {
      logoSVG: require('@/assets/logo3.svg'),
      logoutSVG: require('@/assets/LogoutIcon.svg'),
    }
  },
  computed: {
    ...mapGetters(["isLoggedIn"])
  },
  methods: {
    ...mapMutations(["removeTokens", "verifyRefreshToken"]),
    logout() {
      this.removeTokens()
      this.$router.push({ name: "map" });
    },
    async exportCSVFunction() {
      this.verifyRefreshToken()
      await axios
        .get("/api/v1/map/markers/export_csv", {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`
            },
            responseType: 'blob',
        })
        .then(response => {
            saveAs(response.data, 'DailyUpload.csv');
        })
        .catch(error => {
            this.errors = []
            if (error.response) {
                console.log(JSON.stringify(error))
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
            }
        })
    },
  },
}
</script>

<style scoped>
#navbar-brand-logo {
  width: 2.5em;
  height: auto;
  margin-right: 0.3em;
}

b-navbar {
  background-color: #FFFFFF;
}

.navbar {
  height: 4.2em !important;
}

.nav-link {
  color: #000000 !important;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  margin-right: 1em;
  padding-left: 1em !important;
  padding-right: 1em !important;
}

.router-link-exact-active {
  background-color: #95E375;
  border-radius: 13px;
}

.navbar-brand {
  color: #000000;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 30px;
  background-color: #00000000 !important;
  margin-left: 0.3em;
}

#nav-collapse {
  background-color: #FFFFFF !important;
  border-radius: 13px;
  padding-top: 0.2em;
  padding-bottom: 0.2em;
  z-index: 99999999;
  position: relative;
}

</style>