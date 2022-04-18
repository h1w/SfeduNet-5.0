<template>
    <b-navbar class="navbar" toggleable="lg" type="dark" fixed="top" id="mainNav">
        <div class="container">
            <b-navbar-brand class="navbar-brand" href="#page-top"><img id="logo" src="@/assets/images/logo.png" alt="..." /> <img id="brand" src="@/assets/images/navbar-logo.svg" alt="" /></b-navbar-brand>
            
            <b-navbar-toggle class="navbar-toggler" target="navbarResponsive"></b-navbar-toggle>
            
            <b-collapse class="collapse navbar-collapse" id="navbarResponsive" is-nav>
                <b-navbar-nav class="navbar-nav text-uppercase ms-auto py-4 py-lg-0">
                    <b-nav-item class="nav-item" href="#map">Карта</b-nav-item>
                    <b-nav-item class="nav-item" href="#vol">Волонтерство</b-nav-item>
                    <b-nav-item class="nav-item" href="#about">О Нас</b-nav-item>
                    <b-nav-item class="nav-item" href="#mobile-app">Моб. приложение</b-nav-item>
                    <!-- <b-link active-class="active" class="nav-link"><b-nav-item href="#map">Карта</b-nav-item></b-link>
                    <b-link active-class="active" class="nav-link"><b-nav-item href="#">Волонтерство</b-nav-item></b-link>
                    <b-link active-class="active" class="nav-link"><b-nav-item href="#about">О Нас</b-nav-item></b-link>
                    <b-link active-class="active" class="nav-link"><b-nav-item href="#">Моб. приложение</b-nav-item></b-link> -->
                </b-navbar-nav>
            </b-collapse>

            <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="toggle navigation">
                Menu
                <i class="fas fa-bars ms-a"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav text-uppercase ms-auto py-4 py-lg-0">
                    <li class="nav-item"><a class="nav-link" href="#">#</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">#</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">#</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">#</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">#</a></li>
                </ul>
            </div> -->
        </div>
    </b-navbar>
</template>

<script>
export default {
    mounted() {
      this.$nextTick(function(){
        window.addEventListener("scroll", function(){
          var navbar = document.getElementById("mainNav");
          var nav_classes = navbar.classList;
          if(document.documentElement.scrollTop >= 150) {
            if (nav_classes.contains("shrink") === false) {
              nav_classes.toggle("shrink");
            }
          }
          else {
            if (nav_classes.contains("shrink") === true) {
              nav_classes.toggle("shrink");
            }
          }
        })
      })
    },
}
</script>

<style scoped>
#mainNav {
  padding-top: 1rem;
  padding-bottom: 1rem;
  background-color: #212529;
}
#mainNav .navbar-toggler {
  padding: 0.75rem;
  font-size: 0.75rem;
  font-family: "Montserrat", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  text-transform: uppercase;
  font-weight: 700;
}
#mainNav .navbar-brand {
  color: #ffc800;
  font-family: "Montserrat", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-weight: 700;
  letter-spacing: 0.0625em;
  text-transform: uppercase;
}
#mainNav .navbar-brand img {
  height: 1.5rem;
}
#mainNav .navbar-nav .nav-item .nav-link {
  font-family: "Montserrat", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-size: 0.95rem;
  color: #fff;
  letter-spacing: 0.0625em;
}
#mainNav .navbar-nav .nav-item .nav-link.active, #mainNav .navbar-nav .nav-item .nav-link:hover {
  color: #ffc800;
}

@media (min-width: 992px) {
  #mainNav {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
    border: none;
    background-color: transparent;
    transition: padding-top 0.3s ease-in-out, padding-bottom 0.3s ease-in-out;
  }
  #mainNav .navbar-brand {
    font-size: 1.5em;
    transition: font-size 0.3s ease-in-out;
  }
  #mainNav .navbar-brand #brand {
    height: 2.5rem;
    transition: height 0.3s ease-in-out;
  }
  #mainNav .navbar-brand #logo {
      height: 3.5rem;
      transition: height 0.3s ease-in-out;
  }
  #mainNav.shrink {
    padding-top: 1rem;
    padding-bottom: 1rem;
    background-color: #212529;
  }
  #mainNav.shrink .navbar-brand {
    font-size: 1.25em;
  }
  #mainNav.shrink .navbar-brand svg,
#mainNav.shrink .navbar-brand img {
    height: 1.5rem;
  }
  #mainNav .navbar-nav .nav-item {
    margin-right: 1rem;
  }
  #mainNav .navbar-nav .nav-item:last-child {
    margin-right: 0;
  }
}
</style>