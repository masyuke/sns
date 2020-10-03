$(function(){
  $('.task').draggable();
  $('.todo').droppable();

  $('.task').on('dragstart', (e)=>{
    console.log(e);
  })
  .on('dragstop', (e)=>{
    console.log(e);
  })

  $('.todo').on('drop',(e,ui)=>{
    e.target.appendChild(ui.draggable[0]);
    ui.draggable.removeClass('alert-success').addClass('alert-danger');
    let elem = e.target
    let value = elem.dataset.value;
    //let data = {id: $('#move').text(), status: value};
    let data = {id: $('#move').data('todoid'), status: value};
    $.ajax({
      type: "get",
      url: "move",
      processData: true,
      contentType: false,
      data: data,
      dataType: "json",
    }).done((response) => {
      console.log(response);
    })
  })
});

