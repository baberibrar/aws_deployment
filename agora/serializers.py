from rest_framework import serializers
from mysite.settings import BASE_URL
from .models import Companies, Advocates


class AdvocatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocates
        fields = '__all__'


class RetrieveAdvocatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocates
        fields = ('id', 'name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'company')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        company_data = Companies.objects.filter(id=data['company']).values('id', 'name', 'logo', 'summary')
        data['company'] = {
            'id': company_data[0]['id'],
            'name': company_data[0]['name'],
            'logo': company_data[0]['logo'],
            'href': BASE_URL + '/companies/' + str(company_data[0]['id']) + '/'
        }
        data['links'] = {
            'youtube': instance.youtube,
            'twitter': instance.twitter,
            'github': instance.github
        }
        return data


class CompanyAdvocatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocates
        fields = ('id', 'name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['links'] = {
            'youtube': instance.youtube,
            'twitter': instance.twitter,
            'github': instance.github
        }
        return data


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ['id', 'name', 'logo', 'summary']
