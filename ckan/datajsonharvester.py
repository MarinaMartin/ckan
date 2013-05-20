from ckan.plugins.core import SingletonPlugin, implements
from ckanext.harvest.interfaces import IHarvester

class CKANHarvester(HarvesterBase):
    '''
    A Harvester for Data.json files
    '''
	implements(IHarvester)

    def info(self):
        return {
            'name': 'datajson',
            'title': 'Data.gov Data.json Harvester',
            'description': 'Harvests Data.json files from agencies',
        }

	def validate_config(self, config):
	    '''

	    [optional]

	    Harvesters can provide this method to validate the configuration entered in the
	    form. It should return a single string, which will be stored in the database.
	    Exceptions raised will be shown in the form's error messages.

	    :param harvest_object_id: Config string coming from the form
	    :returns: A string with the validated configuration options
	    '''