const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
toggle?.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? '关闭导航' : '展开导航');
  nav.classList.toggle('open', open);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && nav.classList.contains('open')) {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', '展开导航');
    toggle.focus();
  }
});
document.querySelector('#consult-form')?.addEventListener('submit', event => {
  event.preventDefault();
  const result = document.querySelector('#form-result');
  result.textContent = '演示完成：格式校验通过。信息未发送、未保存，也不会有律师回电。';
  event.target.reset();
  result.focus();
});
