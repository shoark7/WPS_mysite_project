function photoLike(photoId, likeType){
    var url = '/photo/ajx/photo_like/' + photoId + '/' + likeType + '/'
    console.log(url)
    $.ajax({
    method: 'POST',
    url : url,
    })
    .done(function(response) {
        console.log(response);

    })
    .fail(function(response){
        console.log(response);
    });
}
