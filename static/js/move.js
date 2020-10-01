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
    // ドロップした要素を赤い資格に追加する
    e.target.appendChild(ui.draggable[0]);
    // ドロップした要素の色を変更する
    ui.draggable.removeClass('alert-success').addClass('alert-danger');
    // サーバーと非同期で通信
    $.ajax('url',{パラメータ}).done( (res) => {
      // 通信が完了した際に実行する処理を書く
    })
  })
});

