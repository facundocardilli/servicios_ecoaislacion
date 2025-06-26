let sessionId = null;

function jsonRpc(url, method, params) {
    return fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include',
        body: JSON.stringify({
            jsonrpc: '2.0',
            method: 'call',
            params
        })
    }).then(r => r.json());
}

function login() {
    const db = document.getElementById('db').value;
    const login = document.getElementById('loginUser').value;
    const password = document.getElementById('loginPassword').value;
    jsonRpc(`${ODOO_URL}/mobile/session/authenticate`, 'call', { db, login, password })
        .then(res => {
            if (res.result && res.result.uid) {
                sessionId = res.result.session_id;
                localStorage.setItem('session', JSON.stringify({db, session_id: sessionId}));
                document.getElementById('login').classList.add('hidden');
                document.getElementById('main').classList.remove('hidden');
                loadObras();
            } else {
                alert('Error de login');
            }
        });
}

function loadObras() {
    const params = {
        model: 'obras.obra',
        method: 'search_read',
        args: [],
        kwargs: { fields: ['id', 'name'] }
    };
    jsonRpc(`${ODOO_URL}/mobile/dataset/call_kw`, 'call', params)
        .then(res => {
            const select = document.getElementById('obraSelect');
            select.innerHTML = '';
            res.result.forEach(o => {
                const opt = document.createElement('option');
                opt.value = o.id;
                opt.textContent = o.name;
                select.appendChild(opt);
            });
        });
}

function startJornada() {
    const startTime = new Date().toISOString();
    localStorage.setItem('startTime', startTime);
    document.getElementById('startSection').classList.add('hidden');
    document.getElementById('endSection').classList.remove('hidden');
}

function endJornada() {
    const endTime = new Date().toISOString();
    const obraId = document.getElementById('obraSelect').value;
    const materiales = document.getElementById('materiales').value;
    const startTime = localStorage.getItem('startTime');

    const params = {
        model: 'obras.registro_diario',
        method: 'create',
        args: [{
            obra_id: parseInt(obraId),
            fecha: startTime.split('T')[0],
            hora_inicio: startTime,
            hora_fin: endTime,
            observaciones: materiales
        }],
        kwargs: {}
    };
    jsonRpc(`${ODOO_URL}/mobile/dataset/call_kw`, 'call', params)
        .then(() => {
            alert('Registro guardado');
            localStorage.removeItem('startTime');
            document.getElementById('materiales').value = '';
            document.getElementById('startSection').classList.remove('hidden');
            document.getElementById('endSection').classList.add('hidden');
        });
}

document.getElementById('loginButton').addEventListener('click', login);
document.getElementById('startButton').addEventListener('click', startJornada);
document.getElementById('endButton').addEventListener('click', endJornada);

window.addEventListener('load', () => {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js');
    }
});
