// its better to use class, than id  when manupulation of multiple similar elements is needed
// define vars x and y for cs_get class and cs_editable class
console.log('filters.js loaded')
let tr = document.getElementsByClassName("table_row");
let tid = document.getElementsByClassName("t_id");
let tpn = document.getElementsByClassName("t_part_name");
let tpt = document.getElementsByClassName("t_part_type");
let tms = document.getElementsByClassName("t_min_stock");
let tcs = document.getElementsByClassName("t_current_stock");
let too = document.getElementsByClassName("t_on_order");
let teb = document.getElementsByClassName("t_expected_by")
let i,j,k;

function filter(){

    fpn = document.getElementById('fi_part_name').value;
    fpt = document.getElementById('fi_part_type').value;
    foo = document.getElementById('fi_on_order').value;
    console.log("fpn:",fpn,"fpt:", fpt,"foo:", foo);
    // console.log(fpt == "");
    for (i=0; i<= (tr.length); i++) {
        // console.log(i, "|", tpn[i].innerHTML)
        // tr[i].style.display = "none";
        // console.log("i:", i, tid[i].innerHTML, tpn[i].innerHTML, fpn, "::", String(tpn[i].innerHTML.toLowerCase()).includes(fpn.toLowerCase()))
        // console.log(tr[i], i)
        if (fpn != ""){
            if ( String(tpn[i].innerHTML.toLowerCase()).includes(fpn.toLowerCase()) == false ) {
                // console.log(i)
                tr[i].style.display = "none";
            }

        }

        if (fpt != ""){
            if (String(tpt[i].innerHTML.toLowerCase()) != fpt.toLowerCase()) {
                // console.log(i)
                tr[i].style.display = "none";
            }

        }

        if (foo == "1"){
            console.log((too[i].innerHTML) == "")
            if((too[i].innerHTML) == ""){
                tr[i].style.display = "none";
            }
        }
        // console.log(i)
        
    }


}

function filter_revert(){
    console.log(tr.length)
    for (i=1; i < (tr.length+1); i++) {
        // console.log(i);
        tr[i].style.display = "block";
        
    }
}