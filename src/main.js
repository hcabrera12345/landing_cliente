import './style.css'

window.addEventListener('scroll',()=>document.getElementById('nav').classList.toggle('scrolled',scrollY>20));

function toggleMob(){document.getElementById('mob').classList.toggle('open')}
function closeMob(){document.getElementById('mob').classList.remove('open')}
window.toggleMob = toggleMob;
window.closeMob = closeMob;

const trk=document.getElementById('crT'),dots=[...document.querySelectorAll('.dot')];
const cP=document.getElementById('cP'),cN=document.getElementById('cN');
const cDot=document.getElementById('cDot'),cTxt=document.getElementById('cTxt'),hC=document.getElementById('hC');
const LT=[false,false,false,false,true];
const caps=['Puerto costero andino — Tanquero en operación','Estación de Servicio YPFB · Bolivia','Planta de Almacenaje YPFB · Santa Cruz de la Sierra','Puerto Arica · Despacho de Cisternas','Operaciones Regionales — Foto 05'];
let cur=0,tot=5,tmr;

function goTo(i){
  cur=(i+tot)%tot;
  if(trk) trk.style.transform=`translateX(-${cur*100}%)`;
  dots.forEach((d,j)=>d.classList.toggle('on',j===cur));
  if(cTxt) cTxt.textContent=caps[cur];
  const lt=LT[cur];
  if(cP) cP.className='cr-prev '+(lt?'al':'ad');
  if(cN) cN.className='cr-next '+(lt?'al':'ad');
  dots.forEach(d=>{d.classList.toggle('dd',!lt);d.classList.toggle('dl',lt)});
  if(cDot) cDot.style.background=lt?'var(--G)':'#fff';
  if(cTxt) cTxt.style.color=lt?'var(--MUT)':'rgba(255,255,255,.45)';
  if(hC) hC.querySelectorAll('h1,.h-sub,.h-ey-txt').forEach(el=>{
    el.style.color=lt?'var(--BK)':'';
    el.style.textShadow=lt?'none':'';
  });
}

function start(){tmr=setInterval(()=>goTo(cur+1),5500)}
function reset(){clearInterval(tmr);start()}

if(cP) cP.onclick=()=>{goTo(cur-1);reset()};
if(cN) cN.onclick=()=>{goTo(cur+1);reset()};
dots.forEach(d=>d.onclick=()=>{goTo(+d.dataset.i);reset()});

let tx=0;
if(trk) {
  trk.addEventListener('touchstart',e=>tx=e.touches[0].clientX,{passive:true});
  trk.addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>50){goTo(cur+(dx<0?1:-1));reset()}},{passive:true});
}

// Start carousel only if elements exist
if(trk) start();

const obs=new IntersectionObserver(en=>en.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');obs.unobserve(e.target)}}),{threshold:.08});
document.querySelectorAll('.rv').forEach(el=>obs.observe(el));

// ── Formulario de Contacto Web3Forms ──
const form = document.getElementById('contactForm');
if(form){
  form.addEventListener('submit', async function(e){
    e.preventDefault();
    const btn = document.getElementById('submitBtn');
    const success = document.getElementById('formSuccess');
    const error = document.getElementById('formError');

    // Estado de carga
    btn.textContent = 'Enviando...';
    btn.disabled = true;
    btn.style.opacity = '0.7';
    success.style.display = 'none';
    error.style.display = 'none';

    try {
      const data = new FormData(form);
      const res = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        body: data
      });
      const json = await res.json();

      if(json.success){
        success.style.display = 'block';
        form.reset();
      } else {
        error.style.display = 'block';
      }
    } catch(err){
      error.style.display = 'block';
    } finally {
      btn.textContent = 'Enviar Consulta';
      btn.disabled = false;
      btn.style.opacity = '1';
    }
  });
}
