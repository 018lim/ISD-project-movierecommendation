$(document).ready(function(){
    if($('#result') != null){
        Read();
    }
});

function Read(){
    $.ajax({
        url: 'read/',
        type: 'POST',
        async: false,
        data:{
            res: 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
        success: function(response){
            $('#result').html(response);
        }
    });
}

// create
$('#create').on('click', function(){
        $title = $('#title').val();
        $content = $('#content').val();

        if($title == "" || $content == ""){
            alert("Please complete the required field");
        }else{
            $.ajax({
                url: 'create/',
                type: 'POST',
                data: {
                    title: $title,
                    content: $content,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    Read();
                    $('#title').val('');
                    $('#content').val('');
                }
            });
        }
    });

// edit
$(document).on('click', '.edit', function(){
        $id = $(this).attr('name');
        window.location = "edit/" + $id;
    });

// update
$('#update').on('click', function(){
        $title = $('#title').val();
        $content = $('#content').val();

        if($title == "" || $content == ""){
            alert("Please complete the required field");
        }else{
            $id = $('#post_id').val();
            $.ajax({
                url: '../update/' + $id +'/',
                type: 'POST',
                data: {
                    title: $title,
                    content: $content,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    window.location = '../../';
                    alert('Updated!');
                }
            });
        }

    });

// delete

$(document).on('click', '.delete', function(){
        $id = $(this).attr('name');
        $.ajax({
            url: 'delete/' + $id +'/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                Read();
                alert("Deleted!");
            }
        });
    });