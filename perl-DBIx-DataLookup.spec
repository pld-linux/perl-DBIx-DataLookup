#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	DataLookup
Summary:	DataLookup - Perl extension for database view lookup table
Summary(pl.UTF-8):	DataLookup - rozszerzenie Perla do przeglądania widoków baz danych
Name:		perl-DBIx-DataLookup
Version:	0.03
Release:	4
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe4102aa940282b3fe731d37149b73dc
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remotely similar to DBIx::Cache but is very simpler and serves
narrower purpose. This module allows you to both cache records pulled
by an SQL statement from a database in the memory as well as look them
up later at any time during execution of your script.

%description -l pl.UTF-8
Ten moduł zewnętrznie jest podobny do DBIx::Cache, ale jest prostszy i
ma węższy zakres zastosowań. Pozwala na pamiętanie w pamięci rekordów
wyciągniętych z bazy przez wyrażenia SQL, a także przeglądanie ich
później w dowolnej chwili.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}/%{pnam}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"DBIx::DataLookup")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
