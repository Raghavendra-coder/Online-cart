function UpdateCart(page_url, this_ele){
      product_key = this_ele.attr("data-pk")
      action = this_ele.attr("data-action")
      $.ajax({
        url: page_url,
        dataType: "json",
        data: {'a': product_key, 'b': action},
        success: function(data){
          if(data['status'] == false){
            alert(data['message'])
          }
          else{
            if(data['count'] == 0){
              $("#cart").text("")
            }
            else{
              $("#cart").text(data['count'])
            }
            this_ele.parent().html(data['html'])
            $("#popcart").attr('data-bs-content', data['html_cart'])
            showCartCount();

          }
        },
        error: function(data){
          alert("Something went wrong.")
        }

      })
    }
