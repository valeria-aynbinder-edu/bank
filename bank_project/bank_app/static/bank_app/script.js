async function send_delete(branch_id) {

    const response = await fetch('' + branch_id, {method: 'DELETE'});
    if (!response.ok) {
        location.href = '../'
    }

}