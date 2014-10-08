$(document).ready(function() {
    var container = $('#nect-content');
    console.log('success');


    function getPage(pageName) {
        $.ajax({
            url: '/' + pageName + '/',
            type: 'GET',
            success: function(res) {
                container.html(res)
            },
            error: function(e) {
                console.log(e);
            }
        })
    }

    function registerUser(userData) {
        var userInfo = JSON.stringify(userData);
        $.ajax({
            url: '/register/',
            type: 'POST',
            dataType: 'json',
            data: userInfo,
            success: function(res) {
                console.log('successful login');
                console.log(res);
            },
            error: function(e) {
                console.log('login error');
                console.log(e)
            }
        })
    }

    function loginUser(userData) {
        var userInfo = JSON.stringify(userData);
        $.ajax({
            url: '/register/',
            type: 'POST',
            dataType: 'json',
            data: userInfo,
            success: function(res) {
                console.log('successful registration');
                console.log(res);
            },
            error: function(e) {
                console.log('registration error');
                console.log(e)
            }
        })
    }








    $('.nect-login').click(function() {
        getPage('login');
    });

    $('.nect-logout').click(function() {
        getPage('logout');
    });

    $('.nect-register').click(function() {
        getPage('register');
    });

    $('.nect-profile').click(function() {
        getPage('profile');
    });



    $(document).ajaxComplete(function() {
        $('#user_register').submit(function(evt) {
            var userData = {
                'username': evt.target[1].value,
                'email': evt.target[2].value,
                'password1': evt.target[3].value,
                'password2': evt.target[4].value
                };
            evt.preventDefault();
            registerUser(userData);
        });
//        $('#user_login').submit(function(evt) {
//            alert('working?');
//            console.log(userInfo);
//            var userData = {
//                'username': evt.target[1].value,
//                'password': evt.target[2].value
//                };
//            console.log(evt);
//            evt.preventDefault();
//            loginUser(userData);
//        });
    });

});