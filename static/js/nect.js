$(document).ready(function() {
    var container = $('#nect-content');
    console.log('success');

    function getPage(pageName) {
        $.ajax({
            url: '/'+pageName+'/',
            type: 'GET',
            success: function(res) {
                console.log('page success');
                console.log(res);
                container.html(res)
            },
            error: function(e) {
                console.log('page error');
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
        console.log('clicked profile');
        getPage('profile');
    });

    $('#user_register').submit(function(evt) {
        alert('submitting');
        console.log(evt);
        evt.preventDefault();
//        registerUser();
    });

    $('#user_login').submit(function(evt) {
        alert('working?');
        console.log(evt);
        evt.preventDefault();
//        loginUser();
    });
});