import { Modal } from "bootstrap";

export default {
    methods: {
        showErrorModal: function(error,destination,location_id) {
            //Get the loading modal
            var loadingModal = new Modal(document.getElementById('loadingModal'));

            //Hide the loading modal
            loadingModal.hide();

            // Get the error modal
            var elem_cont = document.getElementById("errorModalContent");

            // Update the content
            elem_cont.innerHTML = `<strong>HTML ISSUE:</strong> We could not save the new requirement<hr>${error}`;

            // Show the modal
            var errorModal = new Modal(document.getElementById('errorModal'));
            errorModal.show();
        },
        showValidationErrorModal: function() {
            //Show the error dialog and notify to the user that there were field missing.
            var elem_cont = document.getElementById("errorModalContent");

            // Update the content
            elem_cont.innerHTML =
                `<strong>FORM ISSUE:</strong> Sorry, but can you please fill out the form completely.`;

            // Show the modal
            var errorModal = new Modal(document.getElementById('errorModal'));
            errorModal.show();

        }
    }
}