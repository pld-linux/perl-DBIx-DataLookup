#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	DataLookup
Summary:	DataLookup - Perl extension for database view lookup table
Summary(pl):	DataLookup - rozszerzenie Perla do przegl±dania widoków baz danych
Name:		perl-DBIx-DataLookup
Version:	0.03
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remotely similar to DBIx::Cache but is very simpler and serves
narrower purpose. This module allows you to both cache records pulled
by an SQL statement from a database in the memory as well as look them
up later at any time during execution of your script.

%description -l pl
Ten modu³ zewnêtrznie jest podobny do DBIx::Cache, ale jest prostszy i
ma wê¿szy zakres zastosowañ. Pozwala na pamiêtanie w pamiêci rekordów
wyci±gniêtych z bazy przez wyra¿enia SQL, a tak¿e przegl±danie ich
pó¼niej w dowolnej chwili.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}/%{pnam}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"DBIx::DataLookup")' \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
