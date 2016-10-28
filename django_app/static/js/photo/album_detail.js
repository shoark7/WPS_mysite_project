function photoLike(photoId, likeType){
    var url = '/photo/ajx/photo_like/' + photoId + '/' + likeType + '/'
//    console.log(url)
    $.ajax({
    method: 'POST',
    url : url,
    })
    .done(function(response) {
        var likeCount = response.like_count;
        var dislikeCount = response.dislike_count;
        var spanLikeCount = $('#photo-'+ photoId + '-like-count');
        var spanDislikeCount = $('#photo-'+ photoId + '-dislike-count');
        var userLike = response.user_like;
        var userDislike = response.user_dislike;
        spanLikeCount.text(likeCount);
        spanDislikeCount.text(dislikeCount);

        var btnLike = $('#btn-photo' + photoId + '-like');
        var btnDislike = $('#btn-photo' + photoId + '-dislike');
