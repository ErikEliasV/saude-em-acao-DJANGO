document.addEventListener("DOMContentLoaded",function(){let e=new Date,t=["JANEIRO","FEVEREIRO","MAR\xc7O","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"][e.getMonth()],n=e.getFullYear();document.getElementById("mes-ano").innerHTML=`${t} <br> DE ${n}`,!function e(){let t=document.querySelector(".listin");t.innerHTML="";let n=new Date,l=n.getDay(),a=n.getDate(),i=0===l?-6:1-l;for(let c=0;c<7;c++){let s=new Date(n);s.setDate(a+i+c);let o=`
                <div class="ajeitar-linha">
                    <div class="content">
                        <label class="checkBox">
                            <input class="checkbox" type="checkbox">
                            <div class="transition"></div>
                        </label>
                        <h4>${s.getDate()}</h4>
                    </div>
                </div>
            `;t.innerHTML+=o}let O=new Event("checkboxesGerados");document.dispatchEvent(O)}()});