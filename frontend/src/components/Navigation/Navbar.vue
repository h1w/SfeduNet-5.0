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
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data: function () {
    return {
      logoSVG: require('@/assets/logo.svg')
    }
  },
}
</script>

<style scoped>
#navbar-brand-logo {
  width: 2em;
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