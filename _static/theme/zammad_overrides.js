/* Custom overrides */
/* No oversized <pre>, please - Thanks to @TJemxx */
function shortPre(i) {
   var attr = 'pre-' + i
   var pre = document.getElementById(attr);
   var button = document.getElementById('button-' + attr);

   if ( pre.classList.contains('shorten-pre')) {
      pre.classList.remove('shorten-pre');
      pre.classList.add('release-shorten-pre');

      $(button).html('Reduce to smaller size ...')
   } else {
      pre.classList.remove('release-shorten-pre');
      pre.classList.add('shorten-pre');

      $(button).html('Expand to full size ...')
   }
}

// Update <pre> elements
function WorkPres(item, index) {
   var size = 250;

   if ( !document.getElementById(item) ){
      item.setAttribute('id', 'pre-' + index);
   }

   if( item.clientHeight > size ){
      
      if ( !document.getElementById('button-' + item) ){
         var button = document.createElement('button');
         button.setAttribute('onclick', 'shortPre(' + index + ')');
         button.setAttribute('id', 'button-pre-' + index);
         $(button).html('Expand to full size ...').addClass('shorten-pre-button');      
         item.appendChild(button);

         console.log("added button for big <pre> (pre-" + index + ")")
      }
      
      item.classList.add('shorten-pre');
   }
};

// Provide all tabs with onClick action
function WorkTabs(item) {
   item.setAttribute('onclick', 'CalculatePres()');
}

// Function to fire (re)-calculation for <pre> elements
function CalculatePres(){
   pres = document.getElementsByTagName('pre');
   for(var i = 0; i < pres.length; i++){ 
      WorkPres(pres[i], i);
   };
   console.log("<pre> elements reviewed ...")
}

function AddOnClick(){
   // Find all possible tabs to add onClick actions
   console.log("Add onClick actions for <a>-data-tabs (if any) ...")
   tabs = document.getElementsByTagName('a');
   for(var i = 0; i < tabs.length; i++){ 
      if ( tabs[i].hasAttribute('data-tab') ){
         WorkTabs(tabs[i]);
      }
   };
}

function OnLoadRunner(){
   CalculatePres();
   AddOnClick();
}

// onLoad run through all pres and add shorten classes to those that are quite long
window.addEventListener('load', OnLoadRunner, false);