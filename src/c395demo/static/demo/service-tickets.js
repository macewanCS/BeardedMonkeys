// altering what data is displayed based on the type of service requested
$(document).ready(function() {
    $('#id_request_type').attr('required', true);
    $('#id_request_type').on('change', function () {
        if ($(this).val() === 'Move equipment request') {
            // which system: required
            $('#id_system_label').show();
            $('#id_system').show().attr('required', true);
            // asset tag required
            $('#id_asset_tag_label').show();
            $('#id_asset_tag').show().attr('required', true);
            // move to: required
            $('#id_move_location_label').show();
            $('#id_move_location').show().attr('required', true);
            // everything else is not required
            $('#id_software_label').hide();
            $('#id_software').hide().attr('required', false);
            $('#id_pc_label').hide();
            $('#id_pc').hide().attr('required', false);
            $('#id_description_label').hide();
            $('#id_description').hide().attr('required', false);
        }
        else if ($(this).val() === 'Surplus equipment request') {
            // which system: required
            $('#id_system_label').show();
            $('#id_system').show().attr('required', true);
            // asset tag: required
            $('#id_asset_tag_label').show();
            $('#id_asset_tag').show().attr('required', true);
            // everything is not required
            $('#id_move_location_label').hide();
            $('#id_move_location').hide().attr('required', false);
            $('#id_software_label').hide();
            $('#id_software').hide().attr('required', false);
            $('#id_pc_label').hide();
            $('#id_pc').hide().attr('required', false);
            $('#id_description_label').hide();
            $('#id_description').hide().attr('required', false);
        }
        else if ($(this).val() === 'New software request') {
            // What software: required
            $('#id_software_label').show();
            $('#id_software').show().attr('required', true);;
            // which PC: required
            $('#id_pc_label').show();
            $('#id_pc').show().attr('required', true);;
            // everything else is not required
            $('#id_description_label').hide();
            $('#id_description').hide().attr('required', false);
            $('#id_system_label').hide();
            $('#id_system').hide().attr('required', false);
            $('#id_asset_tag_label').hide();
            $('#id_asset_tag').hide().attr('required', false);
            $('#id_move_location_label').hide();
            $('#id_move_location').hide().attr('required', false);
        } 
        else if ($(this).val() === 'New equipment request') {
            // description: required
            $('#id_description_label').show();
            $('#id_description').show().attr('required', false);
            // everything else is not required
            $('#id_system_label').hide();
            $('#id_system').hide().attr('required', false);
            $('#id_asset_tag_label').hide();
            $('#id_asset_tag').hide().attr('required', false);
            $('#id_move_location_label').hide();
            $('#id_move_location').hide().attr('required', false);
            $('#id_software_label').hide();
            $('#id_software').hide().attr('required', false);
            $('#id_pc_label').hide();
            $('#id_pc').hide().attr('required', false);
        } 
        else {
            // description: required
            $('#id_description_label').show();
            $('#id_description').show().attr('required', false);
            // everything else is not required
            $('#id_system_label').hide();
            $('#id_system').hide().attr('required', false);
            $('#id_asset_tag_label').hide();
            $('#id_asset_tag').hide().attr('required', false);
            $('#id_move_location_label').hide();
            $('#id_move_location').hide().attr('required', false);
            $('#id_software_label').hide().attr('required', false);
            $('#id_software').hide().attr('required', false);
            $('#id_pc_label').hide();
            $('#id_pc').hide().attr('required', false);
        }
    }).change();
});
